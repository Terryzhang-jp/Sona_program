import React, { useState, useEffect } from 'react';
import {jwtDecode} from 'jwt-decode';

function Dashboard() {
    const [userDetails, setUserDetails] = useState({
        userId: '',
        username: '',
        fullName: '',
        image: ''
    });
    const [error, setError] = useState('');

    // 获取用户token并解码以获取用户信息
    useEffect(() => {
        const token = localStorage.getItem("authTokens");
        if (token) {
            try {
                const decoded = jwtDecode(token);
                setUserDetails({
                    userId: decoded.user_id,
                    username: decoded.username,
                    fullName: decoded.full_name,
                    image: decoded.image
                });
            } catch (error) {
                console.error('Error decoding token:', error);
                setError('Failed to decode user details.');
            }
        }
    }, []);

    // 更新信息的处理函数
    const handleUpdateClick = () => {
        // 在这里添加实际的更新信息逻辑
        console.log('Update information clicked');
    };

    return (
        <div className="container py-5">
            <div className="row justify-content-center">
                <div className="col-md-10 col-lg-8">
                    {error && <div className="alert alert-danger" role="alert">{error}</div>}
                    <div className="card border-0 shadow">
                        <div className="card-header bg-primary text-white text-center">
                            <h2 className="mb-0">Your Dashboard</h2>
                        </div>
                        {userDetails.image && 
                            <img src={userDetails.image} className="card-img-top img-fluid rounded-circle mx-auto mt-4" alt="User" style={{ width: '120px', height: '120px', objectFit: 'cover' }} />
                        }
                        <div className="card-body text-center">
                            <h3 className="card-title">{userDetails.fullName || 'User'}</h3>
                            <p className="text-muted">@{userDetails.username}</p>
                            <p><span className="badge badge-light p-2">User ID: {userDetails.userId}</span></p>
                            <button className="btn btn-outline-primary" onClick={handleUpdateClick}>
                                Update Information
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Dashboard;
