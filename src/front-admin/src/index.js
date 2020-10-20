import React, {Component} from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import AdminUI from './AdminUI';

class App extends Component {
  render() {
    return (
      <div className="App">
        <h2>Admin Dashboard</h2>
        <AdminUI handleSubmit={this.handleSubmit} />
      </div>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('root'))