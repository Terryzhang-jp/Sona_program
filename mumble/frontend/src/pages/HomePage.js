import React, { useEffect } from 'react';
import ReactPlaceholder from 'react-placeholder';

import '../styles/components/HomePage.css';

import {
  Contributors,
  FeedCard,
  CreatePost,
  TopicTags,
  PostCardPlaceholder,
  Page,
} from '../components';
import { usersData } from '../data';
import { getPostsForDashboard, resetPostDashboard } from '../actions/postActions';
import { useDispatch, useSelector } from 'react-redux';
import { Button } from '../common';

const HomePage = () => {
  const dispatch = useDispatch();
  const user = usersData.find((u) => Number(u.id) === 1);
  const { posts, next } = useSelector((state) => state.dashboard);
  const isPostsLoading = useSelector((state) => state.dashboard.loading);

  useEffect(() => {
    // 在组件挂载时，发送受保护资源的请求
    fetchProtectedData();
    // 获取首页帖子
    dispatch(getPostsForDashboard());
    return () => dispatch(resetPostDashboard()); // 当组件卸载时清除帖子
  }, [dispatch]);

  const fetchProtectedData = async () => {
    // 发送请求来获取受保护的数据
    // 请确保在此处包含JWT令牌以进行身份验证
  };

  const handleLoadMore = () => {
    if (!next || isPostsLoading) return;

    const searchString = new URL(next).search;
    const params = new URLSearchParams(searchString);
    const page = params.get('page');
    dispatch(getPostsForDashboard(page));
  };

  return (
    <Page>
      <section>
        <CreatePost />
        <ReactPlaceholder
          style={{ width: '100%' }}
          customPlaceholder={<PostCardPlaceholder />}
          showLoadingAnimation
          // 显示帖子，如果加载完成或有帖子存在
          ready={!isPostsLoading || posts.length > 0}
        >
          <FeedCard posts={posts} />
        </ReactPlaceholder>
        {next && (
          // 加载更多按钮
          <Button
            size="lg"
            loading={isPostsLoading}
            onClick={handleLoadMore}
            text={!isPostsLoading ? 'Load More' : 'Loading...'}
          />
        )}
      </section>

      <section>
        <Contributors />
        <TopicTags tags={user.interests} />
      </section>
    </Page>
  );
};

export default HomePage;