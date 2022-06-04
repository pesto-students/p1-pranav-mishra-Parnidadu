import './navbar.css'
export default function Navbar(){
    return(
        <div className="navbar">
            <div>
            <span>
                <h1>shortly</h1>
            </span>
            </div>
            <div className="main">
            <span>
                <label>Feature</label>
                <label>Pricing</label>
                <label>Resource</label>
            </span>
            </div>
            <div>
            <button>Login</button>
            <button>Signup</button>
            </div>
        </div>
    )
}