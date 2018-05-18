import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import './index.css';

import AccordionSegment from '../../Components/AccordionSegment';
import ProjectDataForm from '../../Components/ProjectDetailsForms/ProjectDataForm';
import ProjectAssignmentForm from '../../Components/ProjectDetailsForms/ProjectAssignmentForm';
import ProjectAllocationsForm from '../../Components/ProjectDetailsForms/ProjectAllocationsForm';
import ProjectFinancesForm from '../../Components/ProjectDetailsForms/ProjectFinancesForm';
import { fetchDropdownsActionCreator } from '../../store/actions/fetchDropdowns';

class ProjectDetails extends Component {
  constructor(props){
    super(props);
    this.state = {};
  }

  componentDidMount = () => {
    const action = fetchDropdownsActionCreator(this.props);
    this.props.dispatch(action);
  }

  render() {
    console.log('--------------', this.props);
    return (
      <div className='project-details-container'>
        <AccordionSegment AccordionSegmentTitle="Projectdaten" ><ProjectDataForm project_id={ this.props.match.params.project_id }/></AccordionSegment>
        <AccordionSegment AccordionSegmentTitle="Projektzuteilung" ><ProjectAssignmentForm project_id={ this.props.match.params.project_id } /></AccordionSegment>
        <AccordionSegment AccordionSegmentTitle="Projektablauf" ><ProjectAllocationsForm project_id={ this.props.match.params.project_id } /></AccordionSegment>
        <AccordionSegment AccordionSegmentTitle="Projektfinanzplanung" ><ProjectFinancesForm project_id={ this.props.match.params.project_id } /></AccordionSegment>
      </div>
    )
  }
}

const mapStateToProps = (state, props) => {
  return {
    
  }
}

export default withRouter(connect(mapStateToProps)(ProjectDetails));