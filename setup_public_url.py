import asyncio
import time
from pyngrok import ngrok
import subprocess
import threading

def start_mcp_server():
    """Start the MCP server in a separate thread"""
    subprocess.run(["python", "mcp_server.py"], cwd="T:/puch")

def setup_ngrok_tunnel():
    """Setup ngrok tunnel and return the public URL"""
    try:
        # Start ngrok tunnel on port 8085
        public_tunnel = ngrok.connect(8085)
        public_url = public_tunnel.public_url
        
        # Extract the base URL and add /mcp endpoint
        mcp_url = f"{public_url}/mcp"
        
        print("🌟 NGROK TUNNEL ESTABLISHED!")
        print("=" * 60)
        print(f"🔗 Public MCP URL: {mcp_url}")
        print(f"🔑 Auth Token: 00b577f9f14c")
        print(f"📞 Phone Number: 9440280028")
        print("=" * 60)
        print("\n📝 TO CONNECT WITH PUCH, USE THIS COMMAND:")
        print(f"   /mcp connect {mcp_url} 00b577f9f14c")
        print("=" * 60)
        
        return mcp_url
        
    except Exception as e:
        print(f"❌ Error setting up ngrok: {e}")
        print("\n💡 Alternative: Download ngrok from https://ngrok.com/")
        print("   Then run: ngrok http 8085")
        return None

if __name__ == "__main__":
    print("🚀 Setting up public URL for your MCP server...")
    print("\n⏳ This will:")
    print("   1. Create a public tunnel using ngrok")
    print("   2. Provide you with the connection command for Puch")
    print("   3. Keep the tunnel active")
    
    # Setup ngrok tunnel
    mcp_url = setup_ngrok_tunnel()
    
    if mcp_url:
        print(f"\n✅ Your MCP server is now publicly accessible!")
        print(f"   Keep this script running to maintain the tunnel.")
        print(f"\n🔄 Tunnel Status: Active")
        print(f"   Public URL: {mcp_url}")
        
        try:
            # Keep the script running to maintain the tunnel
            print("\n⌨️  Press Ctrl+C to stop the tunnel")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Shutting down ngrok tunnel...")
            ngrok.disconnect(mcp_url.replace("/mcp", ""))
            print("✅ Tunnel closed.")
    else:
        print("\n❌ Failed to create public tunnel.")
        print("   Please make sure your MCP server is running on port 8085")
