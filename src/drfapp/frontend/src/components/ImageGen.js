import React from 'react'
import imageApi from '../common/imageApi'

class ImageGen extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        text: '',
        color: '',};
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(event) {
    console.log(event)
    this.setState({
      text: event.target.text,
      color: event.target.color,
    })
  }
  handleSubmit(event) {
    data = {
      'text': this.state.text,
      'color': this.state.color,
    }
    imageApi.postText(data)
      .then(response => {
        console.log(response)
      })
      .catch(error => {
        console.log(error)
      })

    alert('A name was submitted text: ' + this.state.text)
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Text:
            <input type="text" value={this.state.text} onChange={this.handleChange} />
          </label>
          <label>
            Color:
            <input type="text" value={this.state.color} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}

export default ImageGen;
