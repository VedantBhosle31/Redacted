import React from 'react'
import "../styles/nav.css"
import Logo from "../assets/logo.svg"

const Nav = () => {
    return (
        <nav>
            <img src={Logo} style={{ height: "50px" }} />
            <p className='name'>EasyDoc</p>

        </nav>
    )
}

export default Nav
