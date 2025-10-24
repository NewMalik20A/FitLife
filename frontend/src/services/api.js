import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

// Articles API
export const articlesApi = {
  getAll: async (category = null) => {
    const url = category ? `${API}/articles?category=${category}` : `${API}/articles`;
    const response = await axios.get(url);
    return response.data;
  },

  getFeatured: async () => {
    const response = await axios.get(`${API}/articles/featured`);
    return response.data;
  },

  getById: async (id) => {
    const response = await axios.get(`${API}/articles/${id}`);
    return response.data;
  },

  create: async (articleData) => {
    const response = await axios.post(`${API}/articles`, articleData);
    return response.data;
  },

  update: async (id, articleData) => {
    const response = await axios.put(`${API}/articles/${id}`, articleData);
    return response.data;
  },

  delete: async (id) => {
    const response = await axios.delete(`${API}/articles/${id}`);
    return response.data;
  }
};

// Categories API
export const categoriesApi = {
  getAll: async () => {
    const response = await axios.get(`${API}/categories`);
    return response.data;
  }
};

// Newsletter API
export const newsletterApi = {
  subscribe: async (email) => {
    const response = await axios.post(`${API}/newsletter/subscribe`, { email });
    return response.data;
  },

  getSubscribers: async () => {
    const response = await axios.get(`${API}/newsletter/subscribers`);
    return response.data;
  }
};

export default {
  articles: articlesApi,
  categories: categoriesApi,
  newsletter: newsletterApi
};