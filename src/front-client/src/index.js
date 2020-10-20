import React, {Component} from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import ClientUI from './ClientUI';

class App extends Component {
  render() {
    return (
      <div className="App">
        <h2>Đặt bánh với Chef Phan</h2>
        <ClientUI handleSubmit={this.handleSubmit} />
      </div>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('root'))