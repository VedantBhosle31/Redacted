import React from 'react'

const Table = () => {

    const data = [
        {
            type: "Receipt",
            date: "4 Mar. 2023",
            time: "1:00 P.M. EST",
            metadata: ":Text",
            user: "John Doe"
        },
        {
            type: "Invoice",
            date: "12 Apr. 2023",
            time: "9:30 A.M. PST",
            metadata: ":Invoice Number 12345",
            user: "Jane Smith"
        },
        {
            type: "Contract",
            date: "27 May 2023",
            time: "2:45 P.M. CST",
            metadata: ":Agreement Terms",
            user: "David Lee"
        },
        {
            type: "Statement",
            date: "8 Jun. 2023",
            time: "11:15 A.M. MST",
            metadata: ":Account Summary",
            user: "Sarah Jones"
        },
        {
            type: "Report",
            date: "19 Jul. 2023",
            time: "4:00 P.M. EST",
            metadata: ":Performance Metrics",
            user: "Michael Brown"
        },
        {
            type: "Proposal",
            date: "3 Aug. 2023",
            time: "10:30 A.M. PST",
            metadata: ":Project Outline",
            user: "Emily Davis"
        },
        {
            type: "Email",
            date: "14 Sep. 2023",
            time: "1:15 P.M. CST",
            metadata: ":Subject: Meeting Confirmation",
            user: "Kevin Wilson"
        },
        {
            type: "Memo",
            date: "25 Oct. 2023",
            time: "3:30 P.M. MST",
            metadata: ":Internal Communication",
            user: "Ashley Garcia"
        },
        {
            type: "Note",
            date: "6 Nov. 2023",
            time: "12:00 P.M. EST",
            metadata: ":Meeting Notes",
            user: "Christopher Rodriguez"
        },
        {
            type: "Document",
            date: "17 Dec. 2023",
            time: "9:45 A.M. PST",
            metadata: ":General Information",
            user: "Jessica Martinez"
        },
        {
            type: "Form",
            date: "28 Jan. 2024",
            time: "2:00 P.M. CST",
            metadata: ":Application Form",
            user: "William Anderson"
        },
        {
            type: "Form",
            date: "28 Jan. 2024",
            time: "2:00 P.M. CST",
            metadata: ":Application Form",
            user: "William Anderson"
        }
    ];

    return (

        <table>
            <tr>
                <th>Type</th>
                <th>Date and time</th>
                <th>Metadata</th>
                <th>User Name</th>
            </tr>
            {
                data.map((e => <tr>
                    <td ><p className='chip'>{e.type}</p> </td>
                    <td>
                        <span style={{ display: "block", paddingBottom: "2px" }}>{e.date}</span>
                        <span style={{ fontSize: "14px", color: "#BAC0C9" }}>{e.time}</span>
                    </td>
                    <td style={{ color: "#A0C0F0" }}>{e.metadata}</td>
                    <td>{e.user}</td>
                </tr>))
            }
        </table>

    )
}

export default Table
