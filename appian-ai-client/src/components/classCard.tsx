
interface Props {
    name: string;
    count: number;
}

const ClassCard = (props: Props) => {
    return (
        <div className="class-card">
            <p>{props.name}</p>
            <p>{props.count}</p>
        </div>
    )
}

export default ClassCard
