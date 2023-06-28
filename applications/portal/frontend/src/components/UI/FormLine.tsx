import React from "react";
import Grid from "@mui/material/Grid";

const FormLine = ({ children }) => {
  const child = React.Children.toArray(children) as React.ReactElement[];
  return (
    <Grid container spacing={3} className="form-line">
      <Grid item lg={6} className="col-1">
        {child[0]}
      </Grid>
      <Grid item lg={6} className="col-2">
        {child[1]}
      </Grid>
    </Grid>
  );
};

export default FormLine;
