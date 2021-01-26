import request from './request'

const imageApi = {

  postText(params) {
    return request({
      url: '/api/v1/image-gen',
      method: 'post',
      data: params
    }).then(({ response }) => {
      return response
    })
  }
}
