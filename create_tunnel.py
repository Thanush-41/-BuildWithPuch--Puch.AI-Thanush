from pyngrok import ngrok
import time

print("🚀 Creating ngrok tunnel for your MCP server...")

try:
    # Create ngrok tunnel
    public_tunnel = ngrok.connect(8085)
    public_url = public_tunnel.public_url
    
    # Create the MCP endpoint URL
    mcp_url = f"{public_url}/mcp"
    
    print("\n" + "="*70)
    print("🌟 SUCCESS! Your MCP server is now publicly accessible!")
    print("="*70)
    print(f"🔗 Public MCP URL: {mcp_url}")
    print(f"🔑 Auth Token: 00b577f9f14c")
    print(f"📞 Phone Number: 9440280028")
    print("="*70)
    print("\n📝 COPY THIS COMMAND FOR PUCH:")
    print(f"   /mcp connect {mcp_url} 00b577f9f14c")
    print("="*70)
    print("\n✅ After connecting with Puch:")
    print("   - Puch will validate your credentials")
    print("   - Puch may generate a custom URL like puch.ai/mcp/xyz123")
    print("   - Keep this tunnel running during the application process")
    
    print(f"\n🔄 Tunnel is active. Press Ctrl+C to stop.")
    
    # Keep tunnel alive
    while True:
        time.sleep(60)  # Check every minute
        
except KeyboardInterrupt:
    print("\n🛑 Stopping ngrok tunnel...")
    ngrok.kill()
    print("✅ Tunnel stopped.")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n💡 Alternative methods:")
    print("1. Download ngrok from https://ngrok.com/")
    print("2. Run: ngrok http 8085")
    print("3. Or use another tunneling service like cloudflared")
