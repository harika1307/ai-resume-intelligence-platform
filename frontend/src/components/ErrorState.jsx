function ErrorState({error}){
    return(
        <div className="error-state">
            <h2>⚠ Analysis Failed</h2>
            <p>{error}</p>
            <span>
                Please check your internet connection or try again.
            </span>
        </div>
    )
}
export default ErrorState;