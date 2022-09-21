import React from "react";
import { makeStyles } from "@mui/styles";
import { vars } from "../../theme/variables";
import {
  Box,
  Container,
  TextField,
  Paper,
  Grid,
  Typography,
  InputAdornment,
} from "@mui/material";
import { AlertIcon } from "../icons";

import StepNavigation from "./StepNavigation";
import { useFormik } from "formik";
import * as yup from "yup";

const { bannerHeadingColor, primaryTextColor } = vars;

const useStyles = makeStyles((theme?: any) => ({
  container: { padding: theme.spacing(10) },
  paper: {
    textAlign: "start",
    border: "1px solid #EAECF0",
    borderRadius: "1rem",
    boxShadow:
      " 0px 12px 16px -4px rgba(16, 24, 40, 0.08), 0px 4px 6px -2px rgba(16, 24, 40, 0.03)",
    padding: "3rem",
  },
  formItem: {
    display: "flex",
    alignItems: "center",
    "& .MuiInputBase-root.MuiOutlinedInput-root": {
      boxShadow: "0px 1px 2px rgba(16, 24, 40, 0.05)",
    },
  },
  header: {
    color: bannerHeadingColor,
    paddingTop: 0,
  },
  label: {
    color: bannerHeadingColor,
    marginBottom: "0.375rem",
  },
  note: {
    color: primaryTextColor,
    fontWeight: 400,
  },
}));

const requiredFieldValidation = yup.string().required("The field is mandatory");

const validationSchema = yup.object().shape({
  identifier: requiredFieldValidation,
  investigatorAndInstitution: requiredFieldValidation,
  name: requiredFieldValidation,
  host: requiredFieldValidation,
  targetSpecies: requiredFieldValidation,
  antibodyTarget: requiredFieldValidation,
  clonality: requiredFieldValidation,
  url: yup
    .string()
    .url("Please enter a valid URL that starts with http or https")
    .required("This field is mandatory"),
});

const Input = ({ formik, label, name, required, placeholder }) => {
  const { errors, touched, getFieldProps, values, handleChange } = formik;
  const classes = useStyles();
  return (
    <>
      <Typography variant="h5" className={classes.label}>
        {label} {required && "(Mandatory)"}
      </Typography>
      <TextField
        fullWidth
        name={name}
        placeholder={placeholder}
        value={values[name]}
        onChange={handleChange}
        {...getFieldProps(name)}
        error={Boolean(touched[name] && errors[name])}
        helperText={touched[name] && errors[name]}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              {touched[name] && errors[name] && <AlertIcon />}
            </InputAdornment>
          ),
        }}
      />
      {!touched[name] && !errors[name] && name === "identifier" && (
        <Typography variant="subtitle1" className={classes.note}>
          Note: Submit unregistered antibodies only
        </Typography>
      )}
    </>
  );
};

const FormLine = ({ children }) => {
  const child = React.Children.toArray(children) as React.ReactElement[];
  return (
    <Grid container spacing={3}>
      <Grid item lg={6}>
        {child[0]}
      </Grid>
      <Grid item lg={6}>
        {child[1]}
      </Grid>
    </Grid>
  );
};
const PersonalForm = (props) => {
  const classes = useStyles();

  const formik = useFormik({
    enableReinitialize: true,
    initialValues: {
      identifier: "",
      investigatorAndInstitution: "",
      url: "",
      name: "",
      host: "",
      targetSpecies: "",
      antibodyTarget: "",
      clonality: "",
      cloneID: "",
      isotype: "",
      conjugate: "",
      format: "",
      uniprotID: "",
      epitope: "",
      applications: "",
      citation: "",
      comments: "",
    },
    validationSchema: validationSchema,
    onSubmit: (values) => {
      console.log("estos son los values", values);
      props.next();
    },
    validateOnChange: true,
    validateOnBlur: true,
  });

  const { handleSubmit } = formik;

  return (
    <form onSubmit={handleSubmit} autoComplete="off">
      <Container maxWidth="xl" className={classes.container}>
        <Paper className={classes.paper}>
          <Grid
            container
            direction="column"
            gap={3}
            m={0}
            width="100%"
            height="100%"
          >
            <Grid item>
              <Typography variant="h1" className={classes.header}>
                2. Antibody Details
              </Typography>
            </Grid>
            <Grid item className={classes.formItem}>
              <FormLine>
                <Box>
                  <Input
                    name="identifier"
                    label="Identifier"
                    required={true}
                    formik={formik}
                    placeholder="An identifier unique to your antibody (e.g. Labname_001 or myab_1023)"
                  />
                </Box>
                <Box>
                  <Input
                    name="investigatorAndInstitution"
                    label="Principal Investigator - Institution or Vendor"
                    required={true}
                    formik={formik}
                    placeholder="(e.g. J. Doe - Harvard)"
                  />
                </Box>
              </FormLine>
            </Grid>
            <Grid item className={classes.formItem}>
              <FormLine>
                <Box>
                  <Input
                    name="url"
                    label="Principal Investigator's/Institution's Website or Vendor Website"
                    required={true}
                    formik={formik}
                    placeholder="http:// or https://"
                  />
                </Box>
                <Box>
                  <Input
                    name="name"
                    label="Antibody name"
                    required={true}
                    formik={formik}
                    placeholder="Anti-phospho-Glo1(Y136) Antibody"
                  />
                </Box>
              </FormLine>
            </Grid>
            <Grid item className={classes.formItem}>
              <FormLine>
                <Box>
                  <Input
                    name="host"
                    label="Host Species"
                    required={true}
                    formik={formik}
                    placeholder="Rabbit"
                  />
                </Box>
                <Box>
                  <Input
                    name="targetSpecies"
                    label="Target/Reactive Species"
                    required={true}
                    formik={formik}
                    placeholder="Mouse"
                  />
                </Box>
              </FormLine>
            </Grid>
            <Grid item className={classes.formItem}>
              <FormLine>
                <Box>
                  <Input
                    name="antibodyTarget"
                    label="Antibody Target"
                    required={true}
                    formik={formik}
                    placeholder="phospho-Glo1(Y136)"
                  />
                </Box>
                <Box>
                  <Input
                    name="clonality"
                    label="Clonality"
                    required={true}
                    formik={formik}
                    placeholder="Polyclonal"
                  />
                </Box>
              </FormLine>
            </Grid>
            <Grid item className={classes.formItem}>
              <FormLine>
                <Box>
                  <Input
                    name="cloneID"
                    label="Clone ID"
                    required={false}
                    formik={formik}
                    placeholder="C200234"
                  />
                </Box>
                <Box>
                  <Input
                    name="isotype"
                    label="Isotype"
                    required={false}
                    formik={formik}
                    placeholder="IgG"
                  />
                </Box>
              </FormLine>
            </Grid>
            <Grid item className={classes.formItem}>
              <FormLine>
                <Box>
                  <Input
                    name="conjugate"
                    label="Conjugate"
                    required={false}
                    formik={formik}
                    placeholder="Alexa Fluor 488"
                  />
                </Box>
                <Box>
                  <Input
                    name="format"
                    label="Antibody Form/Format"
                    required={false}
                    formik={formik}
                    placeholder="glycerol-free"
                  />
                </Box>
              </FormLine>
            </Grid>
            <Grid item className={classes.formItem}>
              <FormLine>
                <Box>
                  <Input
                    name="uniprotID"
                    label="Uniprot ID"
                    required={false}
                    formik={formik}
                    placeholder="Q13255"
                  />
                </Box>
                <Box>
                  <Input
                    name="epitope"
                    label="Epitope"
                    required={false}
                    formik={formik}
                    placeholder="IAVPDV(phosphoY)SA(homoalanine)KRFC"
                  />
                </Box>
              </FormLine>
            </Grid>
            <Grid item>
              <FormLine>
                <Box>
                  <Input
                    name="applications"
                    label="Applications"
                    required={false}
                    formik={formik}
                    placeholder="WB"
                  />
                </Box>
                <Box>
                  <Input
                    name="citation"
                    label="Defining Citation"
                    required={false}
                    formik={formik}
                    placeholder="PMID of paper describing production of antibody"
                  />
                </Box>
              </FormLine>
            </Grid>
            <Grid item>
              <Typography variant="h5" className={classes.label}>
                Comments
              </Typography>
              <TextField
                fullWidth
                name="comments"
                multiline
                rows={5}
                placeholder="Antibody was produced by ... [Insert procedure]"
                value={formik.values.comments}
                onChange={formik.handleChange}
              />
            </Grid>
          </Grid>
        </Paper>
      </Container>
      <StepNavigation
        previous={props.previous}
        next={props.next}
        hasPrevious={props.hasPrevious}
        isLastStep={true}
        activeStep={2}
        formik={formik}
      />
    </form>
  );
};

export default PersonalForm;
