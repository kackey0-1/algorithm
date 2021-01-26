import axios from 'axios'

const service = axios.create({
  baseURL: '127.0.0.1:8000',
  timeout: 300000,
})

export default service;
