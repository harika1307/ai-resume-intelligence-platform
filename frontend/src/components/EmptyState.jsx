function EmptyState(){
    return(
        <div className='empty-state'>
            <h2>🤖 AI Resume Analysis</h2>
            <p>
                Upload your resume and paste a job description
                to generate a detailed ATS analysis.
            </p>
            <ul>
                <li>✅ ATS Score</li>
                <li>✅ Skill Matching</li>
                <li>✅ AI Feedback</li>
                <li>✅ Interview Questions</li>
            </ul>
        </div>
    );
}
export default EmptyState;