import React from 'react'
import ClassCard from './classCard'

const Sidebar = () => {

    const data = [{ name: "Receipts", count: 592 },
    { name: "Resume", count: 254 },
    { name: "Passport", count: 218 },
    { name: "Tax Statement", count: 43 },
    { name: "Balance Sheet", count: 23 },
    { name: "Income Statement", count: 8 },
    { name: "Driving License", count: 2 },]


    return (
        <div className='sidebar'>
            {
                data.map((e => <ClassCard name={e.name} count={e.count} />))
            }

        </div>
    )
}

export default Sidebar
