// frontend/src/utilities/getImageUrl.js


import { getApiUrl } from '../services/config';

export const getImageUrl = (imageUrl) => {
  return imageUrl.startsWith('/images') ? getApiUrl(`static/${imageUrl}`) : imageUrl;
};