using System;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class NarrativeClient : MonoBehaviour
{
    private TcpClient client;
    private NetworkStream stream;

    private void Start()
    {
        try
        {
            client = new TcpClient("127.0.0.1", 65432);
            stream = client.GetStream();
        }
        catch (Exception e)
        {
            Debug.LogError("Failed to connect: " + e.Message);
        }
    }

    public string GetNarrative(string playerAction, string location)
    {
        if (client == null || !client.Connected) 
            return "Error: Not connected to narrative server.";

        // Create JSON request data
        string jsonData = JsonUtility.ToJson(new { action = playerAction, location = location });

        // Send data to Python server
        byte[] data = Encoding.UTF8.GetBytes(jsonData);
        stream.Write(data, 0, data.Length);

        // Receive narrative from Python server
        data = new byte[1024];
        int bytesRead = stream.Read(data, 0, data.Length);
        string response = Encoding.UTF8.GetString(data, 0, bytesRead);

        // Parse JSON response
        var responseDict = JsonUtility.FromJson<NarrativeResponse>(response); 
        return responseDict.narrative; 
    }

    [Serializable]
    private class NarrativeResponse
    {
        public string narrative;
    }

    // ... other methods for handling narrative in Unity
}
