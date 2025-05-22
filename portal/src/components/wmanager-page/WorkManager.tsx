import './WorkManager.css'

interface WorkManagerProps{
    json:any;
}

const WorkManager = ({json}:WorkManagerProps) => {
    return <>
        <iframe className="workload-manager-frame" title="Workload Manager App" src={`http://work-manager.default.svc.cluster.local:31007`}></iframe>
        </>
};


export default WorkManager;