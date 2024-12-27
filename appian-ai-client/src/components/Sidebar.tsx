import React from 'react'
import ClassCard from './classCard'

const Sidebar = () => {

    const data = [{ name: "Aadhar Card", count: 592 },
    { name: "Credit card Application", count: 254 },
    { name: "Bank Account Application", count: 218 },
    { name: "Pan card", count: 43 },
    { name: "Voter ID", count: 23 },
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
