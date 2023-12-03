import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import { login } from '../actions/authActions';
import { useForm } from '../hooks';
import { Button, Input, Message } from '../common';

const LoginForm = () => {
  let dispatch = useDispatch();

  let auth = useSelector((state) => state.auth);
  let { error } = auth;

  // 使用电子邮件字段替换用户名字段
  const [formValues, fieldChanges] = useForm({ email: '', password: '' });
  const onSubmit = (e) => {
    e.preventDefault();
    dispatch(login(formValues));
  };

  return (
    <>
      {error && <Message variant="error">{error}</Message>}

      <form className="form" onSubmit={onSubmit} style={{ width: '100%' }}>
        <Input
          name="email"
          value={formValues.email}
          onChange={fieldChanges}
          required={true}
          label="Email:" // 将标签改为"Email"
          type="email" // 设置输入类型为电子邮件
        />
        <Input
          name="password"
          value={formValues.password}
          type="password"
          onChange={fieldChanges}
          required={true}
          label="Password:"
        />
        <Button color="main" type="submit" text="Login" size="lg" loading={auth?.isLoading} />
        <span style={{ marginLeft: '1rem' }}>
          New here? <Link to="/signup">Sign up</Link>
        </span>
      </form>

      <Link style={{ marginTop: '1.5rem' }} to="/forgot-password">
        Forgot Password?
      </Link>
    </>
  );
};

export default LoginForm;