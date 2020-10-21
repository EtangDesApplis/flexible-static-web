import React, {Component} from 'react';
import config from './config.json';

class ClientUI extends Component {
  constructor(props) {
    super(props);
    this.state = {name: '',
                  phone: '',
                 };
    this.handleName = this.handleName.bind(this);
    this.handlePhone = this.handlePhone.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  
  handleName(event) {    
    this.setState({name: event.target.value});  
  }

  handlePhone(event) {    
    this.setState({phone: event.target.value});  
  }

  handleSubmit(event) {
    //https://jasonwatmore.com/post/2020/02/01/react-fetch-http-post-request-examples
    //for timeout https://www.npmjs.com/package/fetch-timeout
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      //body: JSON.stringify({ title: 'React POST Request Example' })
      body: JSON.stringify({ name: this.state.name, phone: this.state.phone })
    };
    fetch(config.backend+"/create/",requestOptions)
      .then(response => response.json())
      //wait til the reponse from back end
      .then(data => {
        console.log(data)
        this.setState({name: ''});
        this.setState({phone: ''});
      });

    event.preventDefault();
  }
  
  render() {
      return (
        <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Name:
            <input type="text" value={this.state.name} onChange={this.handleName} />        </label>
          <label>
            Phone:
            <input type="text" value={this.state.phone} onChange={this.handlePhone} />        </label>
          <input type="submit" value="Order" />
        </form>
        </div>
      );
  }
}

export default ClientUI;