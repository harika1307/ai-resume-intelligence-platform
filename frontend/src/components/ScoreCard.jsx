
function ScoreCard({analysisResult}){
    return(
        <div className='score-card'>
            <h2>ATS Score </h2>
            <p className='score-number'>{analysisResult.ats_score}%</p>
            <span className='score-status'>
                {
                analysisResult.ats_score>=80?"🟢 Excellent Match":analysisResult.ats_score>=60?"🟡 Good Match"
        :"🔴 Needs Improvement"
                }
            </span>
            <hr/>
            <div className='score-info'>
                <p>
                Matched:
                {analysisResult.matched_skills.length}
                </p>
                <p>
                Missing:
                {analysisResult.missing_skills.length}
                </p>
            </div>
        </div>
    );
}
export default ScoreCard;