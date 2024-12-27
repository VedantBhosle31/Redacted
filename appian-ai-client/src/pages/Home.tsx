import React from 'react'
import "../styles/home.css"
import Sidebar from '../components/Sidebar'
import SearchBar from '../components/SearchBar'
import Table from '../components/Table'

const Home = () => {
    return (
        <div style={{ maxHeight: '100%', overflow: 'hidden' }}>
            <div className='header'>
                <div className='left-cont'>
                    <h2>Documents</h2>
                    <p style={{ color: "#B4BFCD" }}>check and filter documents here </p>
                </div>
                <button className='btn'>New Document</button>
            </div>
            <div className='bottom-cont'>
                <Sidebar />
                <div className='bottom-right'>
                    <SearchBar />
                    <div className='table'>
                        <Table />
                    </div>

                </div>

            </div>
        </div>
    )
}

export default Home
