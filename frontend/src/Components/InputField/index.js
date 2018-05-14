import React, { Component } from 'react';

/* 
  Example of the InputField component
<InputField 
  className='project-data-form'
  required='True'
  type='text'
  name='name'
  placeholder='Project Name'
  onChange={ this.handleChange }
  value={ this.state.name }
  updateParentState={ this.someFunction }
> 
*/

class InputField extends Component{

  constructor(props) {
    super(props);

    this.state = {
      value: '' 
    }
  }

  handleChange = (e) => {
    this.props.updateParentState([this.props.name, e.target.value])
    this.setState({
      value: e.target.value,
    })
  }

  render() {
    return (
      <div className={ this.props.className + '__input-container' }>
        <label>{ this.props.placeholder }{ this.props.required === 'true' ? <span>*</span> : '' }</label>
        <p className={ this.props.className + '__validation-message generic-validation-message hidden-element'} >{ 'Incorrect ' + this.props.placeholder }</p>
        <input
          className={ this.props.className + '__input' }
          type={ this.props.type }
          name={ this.props.name }
          placeholder={ this.props.placeholder }
          onChange={ this.handleChange }
          value={ this.state.value }
        />
      </div>
    )
  }
}

export default InputField;