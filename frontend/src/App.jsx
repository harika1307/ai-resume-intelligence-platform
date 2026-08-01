import { useState } from 'react';
import './App.css';
import api from './services/api';
import ScoreCard from './components/ScoreCard';
import SkillCard from './components/SkillCard';
import FeedbackCard from './components/FeedbackCard';
import EmptyState from './components/EmptyState';
import LoadingState from './components/LoadingState';
import ErrorState from './components/ErrorState';
function App() {
  
  const [jobDescription,setJobDescription]=useState("");
  const [resumeFile,setResumeFile]=useState(null);
  const [analysisResult,setAnalysisResult]=useState(null);
  const [loading,setLoading]=useState(false);
  const [error,setError]=useState("");
  const handleAnalyze=async () => {
    setError("");
    if(!resumeFile){
      setError("Please upload your resume.");
    }
    if(!jobDescription.trim()){
      setError("Please paste the job description.");
    }
    setLoading(true)

    setAnalysisResult(null)
    
    
    const formdata=new FormData()
    formdata.append("file",resumeFile)
    formdata.append("job_description",jobDescription)
    try{
        const response=await api.post("/ats/analyze",formdata)
        setAnalysisResult(response.data)
        setError("");
    } catch(error){ 
        console.error(error)
    }
    finally{
      setLoading(false)
    }
    
  }
  
  return (
    <div className='app'>
      <div className='container'>
        <h1>🤖 AI Resume Intelligence Platform</h1>
        <p className='subtitle'>Smart ATS Analysis & Resume Optimization</p>
        <div className='upload-section'>
          <p>
            Upload your resume and analyze it against any job description.
          </p>
          <h3>Resume</h3>
          <label className='file-upload'>
            <input type="file" disabled={loading} onChange={(e)=>setResumeFile(e.target.files[0])}/>
            <span>📤 Upload Resume</span>
          </label>
          {
            resumeFile && (
              <div className="file-name">
                <p>✅ Resume Selected</p>
                <span>{resumeFile.name}</span>
              </div>
            )
          }
          
          <h3>Paste Job Description</h3>
          <textarea rows="10" cols="60" disabled={loading} placeholder="Paste the complete job description here..." value={jobDescription} onChange={(e)=>setJobDescription(e.target.value)}></textarea>
          {
            error && (
              <p className='error-message'>⚠ {error}</p>
            )
          }
          <button onClick={handleAnalyze} disabled={loading}>{loading?"⏳ Analyzing...":"🚀 Analyze Resume"}</button>
        </div>
        <div className='results-section'>
          {
            !analysisResult && !loading && (
              <EmptyState />
            )
          }
          {
            loading && (
              <LoadingState/>
            )
          }
          {error && (
            <ErrorState error={error}/>
          )}
          {
            analysisResult && (
              <div className='results-grid'>
                <ScoreCard analysisResult={analysisResult}/>
                <SkillCard
                    title="Matched Skills"
                    skills={analysisResult.matched_skills}
                    icon="✔"
                    className="matched-card"
                />

                <SkillCard
                    title="Missing Skills"
                    skills={analysisResult.missing_skills}
                    icon="❌"
                    className="missing-card"
                />

                <SkillCard
                    title="Extra Skills"
                    skills={analysisResult.extra_skills}
                    icon="⭐"
                    className="extra-card"
                />
                            
                
                <FeedbackCard
                    title="Strengths"
                    items={analysisResult.ai_feedback.strengths}
                    icon="💪"
                    className="strength-card"
                />

                <FeedbackCard
                    title="Weaknesses"
                    items={analysisResult.ai_feedback.weaknesses}
                    icon="⚠️"
                    className="weakness-card"
                />

                <FeedbackCard
                    title="Resume Improvements"
                    items={analysisResult.ai_feedback.resume_improvements}
                    icon="📝"
                    className="improvement-card"
                />

                <FeedbackCard
                    title="Keyword Suggestions"
                    items={analysisResult.ai_feedback.keyword_suggestions}
                    icon="🔑"
                    className="keyword-card"
                />

                <FeedbackCard
                    title="Learning Roadmap"
                    items={analysisResult.ai_feedback.missing_skill_suggestions}
                    icon="🎯"
                    className="suggestion-card"
                />

                <FeedbackCard
                    title="Interview Questions"
                    items={analysisResult.ai_feedback.interview_questions}
                    icon="❓"
                    className="interview-card"
                />
              </div>
            )
          }
        </div>
      </div>
      
    </div>
  )
}

export default App
