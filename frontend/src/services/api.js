import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
});

export const getItems = async () => {
  try {
    const response = await api.get('/items');
    return response.data;
  } catch (error) {
    console.error('Error fetching items:', error);
    throw error;
  }
};
