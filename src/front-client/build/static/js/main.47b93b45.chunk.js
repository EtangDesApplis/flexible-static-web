(this["webpackJsonpreact-tutorial"]=this["webpackJsonpreact-tutorial"]||[]).push([[0],{14:function(e,t,n){},15:function(e,t,n){"use strict";n.r(t);var a=n(2),l=n(3),i=n(5),r=n(4),h=n(0),u=n.n(h),c=n(7),o=n.n(c),s=(n(14),n(1)),m=n(8),b=function(e){Object(i.a)(n,e);var t=Object(r.a)(n);function n(e){var l;return Object(a.a)(this,n),(l=t.call(this,e)).state={name:"",phone:""},l.handleName=l.handleName.bind(Object(s.a)(l)),l.handlePhone=l.handlePhone.bind(Object(s.a)(l)),l.handleSubmit=l.handleSubmit.bind(Object(s.a)(l)),l}return Object(l.a)(n,[{key:"handleName",value:function(e){this.setState({name:e.target.value})}},{key:"handlePhone",value:function(e){this.setState({phone:e.target.value})}},{key:"handleSubmit",value:function(e){var t=this,n={method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({name:this.state.name,phone:this.state.phone})};fetch(m.backend+"/create/",n).then((function(e){return e.json()})).then((function(e){console.log(e),t.setState({name:""}),t.setState({phone:""})})),e.preventDefault()}},{key:"render",value:function(){return u.a.createElement("div",null,u.a.createElement("form",{onSubmit:this.handleSubmit},u.a.createElement("label",null,"Name:",u.a.createElement("input",{type:"text",value:this.state.name,onChange:this.handleName}),"        "),u.a.createElement("label",null,"Phone:",u.a.createElement("input",{type:"text",value:this.state.phone,onChange:this.handlePhone}),"        "),u.a.createElement("input",{type:"submit",value:"Order"})))}}]),n}(h.Component),d=function(e){Object(i.a)(n,e);var t=Object(r.a)(n);function n(){return Object(a.a)(this,n),t.apply(this,arguments)}return Object(l.a)(n,[{key:"render",value:function(){return u.a.createElement("div",{className:"App"},u.a.createElement("h2",null,"\u0110\u1eb7t b\xe1nh v\u1edbi Chef Phan"),u.a.createElement(b,{handleSubmit:this.handleSubmit}))}}]),n}(h.Component);o.a.render(u.a.createElement(d,null),document.getElementById("root"))},8:function(e){e.exports=JSON.parse('{"backend":"back"}')},9:function(e,t,n){e.exports=n(15)}},[[9,1,2]]]);
//# sourceMappingURL=main.47b93b45.chunk.js.map