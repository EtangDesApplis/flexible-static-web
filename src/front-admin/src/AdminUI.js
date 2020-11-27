import React, {Component} from 'react';
import config from './config.json';
import kcconfig from './keycloak.json';
import Keycloak from 'keycloak-js';

class AdminUI extends Component {
  constructor(props) {
    super(props);
    this.state = {
                  data: '',
                  keycloak: null,
                  authenticated: false
                 };
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    const keycloak = Keycloak(kcconfig);
    keycloak.init({onLoad: 'login-required'}).then(authenticated => {
      this.setState({ keycloak: keycloak, authenticated: authenticated })
    })
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
    if(this.state.keycloak){
      if(this.state.authenticated) return(
        <div>
        <form onSubmit={this.handleSubmit}>
          <input type="submit" value="Show Database" />
        </form>
        <p>{this.state.data}</p>
        </div>
      ); else return(<div>Unable to authenticate!</div>);
    }
    return (
      <div>Initializing Keycloak ...</div>
    );
  }
}

export default AdminUI;