


function FeedbackCard({title,items,icon,className}){
    return(
        <div className={`card ${className}`}>
            <h3>{title}</h3>
            <ul>
            {
                items.map((iq)=>(
                    <li key={iq}>
                        <span>{icon}</span>
                        <span>{iq.name}</span>
                    </li>
                ))
            }
            </ul>
        </div>
    )
}
export default FeedbackCard;