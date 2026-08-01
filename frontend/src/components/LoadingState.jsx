function LoadingState(){
    return (
        <div className="loading-state">
            <div className="loader"></div>
            <h2>Analyzing Resume...</h2>
            <p>🔍 Parsing Resume...</p>
            <p>⚡ Matching Skills...</p>
            <p>🤖 Generating AI Feedback...</p>
            <p>📋 Preparing Interview Questions...</p>
            <span>Please wait a few seconds...</span>
        </div>

    );
}
export default LoadingState;