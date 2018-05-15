import React, { Component } from 'react';
import './index.css';

import Header from '../../Components/Header'
import Button from '../../Components/Button';
import SearchBox from '../../Components/SearchBox';
import Nav from '../../Components/Nav';
import LoginForm from "../../Components/LoginForm";
import AccordionSegment from '../../Components/AccordionSegment';

class App extends Component {
  render() {
    return (
      <div>
        <Header />
        <Button btnText="Button"/>
        <SearchBox />
        <Nav />
        <LoginForm/>
        <br/>
        <AccordionSegment AccordionSegmentTitle="Data Category"/>
        <AccordionSegment AccordionSegmentTitle="Data Category"/>
        <AccordionSegment AccordionSegmentTitle="Data Category"/>
        <AccordionSegment AccordionSegmentTitle="Data Category"/>
      </div>
    );
  }
}

export default App;