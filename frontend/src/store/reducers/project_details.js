import { SET_PROJECT_DETAILS } from '../constants';

const initialState = {};

export const project_details = (state = initialState, action) => {
  switch (action.type) {
    case SET_PROJECT_DETAILS: {
      return action.payload.project_details;
    }
    default:
      return state;
  }
};
