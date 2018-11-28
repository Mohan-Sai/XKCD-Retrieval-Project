using Microsoft.AspNetCore.Hosting;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace XKCDRetrieval.Models
{
    public class InvertedIndex : IInvertedIndex
    {
        private IHostingEnvironment env;
        public dynamic jsonData;
        public InvertedIndex(IHostingEnvironment hostingEnvironment)
        {
            env = hostingEnvironment;
            var fileProvider = env.WebRootFileProvider;

            var fileInfo = fileProvider.GetFileInfo("InvIndex1.json");

            var fileStream = fileInfo.CreateReadStream();
            
            using (var reader = new StreamReader(fileStream))
            {
                using (JsonReader sr = new JsonTextReader(reader))
                {
                    JsonSerializer serializer = new JsonSerializer();

                    jsonData = serializer.Deserialize(sr);
                }
            }
        }
    }
}
