// frontend/src/utilities/RouteHandler.js

import { useHistory } from 'react-router';
import { useLocationBlocker } from '../hooks';

const RouteHandler = ({ children }) => {
  const history = useHistory();
  useLocationBlocker(history);
  return <>{children}</>;
};

export default RouteHandler;