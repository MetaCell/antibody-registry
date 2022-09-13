import React from "react";
import "./styles/style.less";
import { CssBaseline } from "@mui/material";
import { ThemeProvider } from "@mui/material/styles";
import theme from "./theme/Theme";
import Navbar from "./components/NavBar/Navbar";
import About from "./components/About";
import Home from "./components/Home";
import AntibodyDetail from "./components/AntibodyDetail";
import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";
import FAQs from "./components/Support/FAQs";
import ContactUs from "./components/Support/ContactUs";
import TermsAndConditions from "./components/Support/TermsAndConditions";
import { getCurrentUser } from "./services/UserService";

const App = () => {
  getCurrentUser();
  return (
    <BrowserRouter>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Navbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/about" component={About} />
          <Route path="/login">
            <Redirect to="/" />
          </Route>
          <Route path="/:antibody_id(AB_.*)" component={AntibodyDetail} />
          <Route path="/faq" component={FAQs} />
          <Route path="/contact-us" component={ContactUs} />
          <Route path="/terms-and-conditions" component={TermsAndConditions} />
        </Switch>
      </ThemeProvider>
    </BrowserRouter>
  );
};

export default App;
