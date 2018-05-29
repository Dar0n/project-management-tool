import { validateTokens } from "./validateTokens";
import { SERVER_URL } from "../constants";
import { getProjectDetailsAction } from './getProjectDetailsAction';
import { getProjectMilestonesAction } from './getProjectMilestonesAction';
import alertify from 'alertify.js';

export const postProjectMilestone = (props, body, method, milestone_id) => (dispatch, getState) => {
  validateTokens(getState(), dispatch, props)
  .then(response => {
    const headers = ({
      Authorization: `Bearer ${getState().tokens.access}`,
      'content-type': 'application/json',
    });
    const config = {
      method,
      headers,
      body: JSON.stringify(body),
    }
    let url;
    if (method === 'PATCH') url = `${SERVER_URL}project_milestones/${milestone_id}/`
    else if (method === "POST") url = `${SERVER_URL}project_milestones/new/`
    return fetch(url, config);
  })
  .then(response => {
    if (response.ok) {
      const fetchURL = `${SERVER_URL}project_milestones/milestones/${props.project_id}/`
      dispatch(getProjectDetailsAction(props));
      dispatch(getProjectMilestonesAction(props, fetchURL));
      alertify.delay(3000).success('Erfolgreich gespeichert');
    } else {
      alertify.delay(3000).error('Es ist ein Fehler aufgetreten. Versuchen Sie es erneut.')
    }
  })
  
}
