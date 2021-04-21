import React, { Component } from 'react';
import './style.css';

class Home extends Component {
  constructor(props) {
    super(props);

    this.state = {
      time: null
    };

    fetch('/time')
      .then(res => res.json())
      .then(data => {
        const time = data.time;
        this.setState({ time });
      });
  }

  render() {
    return (
      <div>
        <h1>Home</h1>
        <div>{this.state.time}</div>
      </div>
    )
  }
}

export default Home;