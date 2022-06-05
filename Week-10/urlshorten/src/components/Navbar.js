import './navbar.css'
import {
    BrowserRouter as Router,
    Routes as Switch,
    Route,
    Link
  } from "react-router-dom";
import Pricing from './Pricing';
import Resources from './Resources';
import Feature from './Feature';
export default function Navbar(){
    return(
        <Router>
        <div className="navbar">
                <div>
                <span>
                    <h1>shortly</h1>
                </span>
                </div>
                
                <div className="main">
                <span>
                    <Link to='/feature'>Feature</Link>
                    <Link to='/pricing'>Pricing</Link>
                    <Link to='/resources'>Resource</Link>
                </span>
                </div>
                <div>
                <button>Login</button>
                <button>Signup</button>
                </div>
                <Switch>
                    <Route path="/feature">
                        <Feature />
                    </Route>
                    <Route path="/pricing">
                        <Pricing />
                    </Route>
                    <Route path="/resources">
                        <Resources />
                    </Route>
                </Switch>
            
        </div>
        </Router>
    )
}