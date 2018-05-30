import React, { Component } from 'react';
import './index.css';
import { Link } from 'react-router-dom';
import logo from '../../assets/logo.jpg'

class Header extends Component {
  render() {
    return (
      <div className='header'>
        <Link to="/overview">{ logo }</Link>
        <h1>Matryoshka</h1>
      </div>
    )
  }
}

export default Header;