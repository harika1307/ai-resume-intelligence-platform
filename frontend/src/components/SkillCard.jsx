


function SkillCard({title,skills,icon,className}){
    return(
        <div className={`card ${className}`}>
            <h2>{title}</h2>
            <ul>
                {
                skills.map((skill)=>(
                    <li key={skill.name}>
                        <span>{icon}</span>
                        <span>{skill.name}</span>
                    </li>
                ))
                }
            </ul>
        </div>
    )
}
export default SkillCard;