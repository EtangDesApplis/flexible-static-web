import React, {Component} from 'react';
import config from './config.json';

class AdminUI extends Component {
  constructor(props) {
    super(props);
    this.state = {
                  data: ''
                 };
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    fetch(config.backend+"/read/")
      .then(response => response.json())
      //wait til the reponse from back end
      .then(data => {
        console.log(data)
        this.setState({data: JSON.stringify(data)});
      });

    event.preventDefault();
  }
  
  render() {
      return (
        <div>
        <form onSubmit={this.handleSubmit}>
          <input type="submit" value="Show Database" />
        </form>
      <p>{this.state.data}</p>
        </div>
      );
  }
}

export default AdminUI;