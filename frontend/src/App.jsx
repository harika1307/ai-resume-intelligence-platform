import { useState } from 'react';
import './App.css';
import api from './services/api';
function App() {
  
  const [jobDescription,setJobDescription]=useState("");
  const [resumeFile,setResumeFile]=useState(null);
  const [analysisResult,setAnalysisResult]=useState(null);
  const [loading,setLoading]=useState(false);
  const handleAnalyze=async () => {
    setLoading(true)
    console.log("Analyze button clicked!")
    const formdata=new FormData()
    formdata.append("file",resumeFile)
    formdata.append("job_description",jobDescription)
    try{
        const response=await api.post("/ats/analyze",formdata)
        setAnalysisResult(response.data)
    } catch(error){ 
        console.error(error)
    }
    finally{
      setLoading(false)
    }
    
  }
  return (
    <div>
      <h1>AI Resume Intelligence Platform</h1>
      <p>
        Upload your resume and analyze it against any job description.
      </p>
      <h3>Resume</h3>
      <input type="file" onChange={(e)=>setResumeFile(e.target.files[0])}/>
      <br/><br/>
      <h3>Job Description</h3>
      <textarea rows="10" cols="60" placeholder="Paste the job description here..." value={jobDescription} onChange={(e)=>setJobDescription(e.target.value)}></textarea>
      <br/><br/>
      <button onClick={handleAnalyze} disabled={loading}>{loading?"Analyzing...":"Analyze Resume"}</button>
      <h2>ATS Score</h2>
      <p>
        {analysisResult ? analysisResult.ats_score: "No analysis yet"}
      </p>
      
    </div>
  )
}

export default App
