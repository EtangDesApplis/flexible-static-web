(this["webpackJsonpreact-tutorial"]=this["webpackJsonpreact-tutorial"]||[]).push([[0],{10:function(t,e,n){t.exports=n(17)},15:function(t,e,n){},17:function(t,e,n){"use strict";n.r(e);var a=n(1),i=n(2),c=n(5),l=n(4),u=n(0),r=n.n(u),o=n(7),s=n.n(o),h=(n(15),n(3)),d=n(8),m=n(9),b=n.n(m),p=function(t){Object(c.a)(n,t);var e=Object(l.a)(n);function n(t){var i;return Object(a.a)(this,n),(i=e.call(this,t)).state={data:"",keycloak:null,authenticated:!1},i.handleSubmit=i.handleSubmit.bind(Object(h.a)(i)),i}return Object(i.a)(n,[{key:"componentDidMount",value:function(){var t=this,e=b()("/keycloak.json");e.init({onLoad:"login-required"}).then((function(n){t.setState({keycloak:e,authenticated:n})}))}},{key:"handleSubmit",value:function(t){var e=this;fetch(d.backend+"/read/").then((function(t){return t.json()})).then((function(t){console.log(t),e.setState({data:JSON.stringify(t)})})),t.preventDefault()}},{key:"render",value:function(){return this.state.keycloak?this.state.authenticated?r.a.createElement("div",null,r.a.createElement("form",{onSubmit:this.handleSubmit},r.a.createElement("input",{type:"submit",value:"Show Database"})),r.a.createElement("p",null,this.state.data)):r.a.createElement("div",null,"Unable to authenticate!"):r.a.createElement("div",null,"Initializing Keycloak ...")}}]),n}(u.Component),f=function(t){Object(c.a)(n,t);var e=Object(l.a)(n);function n(){return Object(a.a)(this,n),e.apply(this,arguments)}return Object(i.a)(n,[{key:"render",value:function(){return r.a.createElement("div",{className:"App"},r.a.createElement("h2",null,"Admin Dashboard"),r.a.createElement(p,{handleSubmit:this.handleSubmit}))}}]),n}(u.Component);s.a.render(r.a.createElement(f,null),document.getElementById("root"))},8:function(t){t.exports=JSON.parse('{"backend":"http://localhost:5000"}')}},[[10,1,2]]]);
//# sourceMappingURL=main.111e68fa.chunk.js.map