import * as React from "react";
import { hot } from "react-hot-loader";
import { Home } from '../containers/Home';
import { About } from '../containers/About';

import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import { AppLayout } from "../layouts/AppLayout";

export const Routes = () => {
  return (
    <Router>
        <Switch>
            <AppLayout>
                <Route exact path="/" render={(props: any) => <Home {...props} /> } />
                <Route exact path="/about" render={(props: any) => <About {...props} /> } />
          </AppLayout>
        </Switch>
    </Router>
  );
}

export default hot(module)(Routes);
