using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using XKCDRetrieval.Models;
using Microsoft.AspNetCore.Rewrite.Internal.ApacheModRewrite;
using Porter2Stemmer;

namespace XKCDRetrieval.Controllers
{

    public class IndexController : Controller
    {
        private InvertedIndex invIndex;
        EnglishPorter2Stemmer ps;
        public IndexController(IInvertedIndex invertedIndex)
        {
            ps = new EnglishPorter2Stemmer();
            invIndex = (InvertedIndex)invertedIndex;
        }
        [Route("")]
        public IActionResult Index()
        {
            //List<float> l = (List<float>)ViewData["List"];
            //if (l != null)
            //    ViewData["List"] = l;
            return View();
        }
        [Route("[controller]/[action]")]
        public IActionResult Search(SearchViewModel viewModel)
        {
            var searchTokens = viewModel.search.Split(" ");
            List<string> stemmedTokens = new List<string>();
            foreach (string s in searchTokens)
            {
                stemmedTokens.Add(ps.Stem(s).Value);
            }
            List<List<float>> links = new List<List<float>>();
            foreach (string s in stemmedTokens)
            {
                JArray j = new JArray();
                

                List<float> index = new List<float>();
                try
                {
                    index = invIndex.jsonData[s].ToObject<List<float>>();

                }
                catch
                {
                    continue;
                }
                links.Add(index);
            }
            List<float> commonList = new List<float>();
            int ctr = 0;
            foreach (List<float> l in links)
            {
                if (ctr == 0)
                {
                    commonList.AddRange(l);
                    ctr++;
                    continue;
                }
                commonList = commonList.Intersect<float>(l).ToList();
            }
            foreach(var i in links)
            {
                foreach(float f in i)
                {
                    if (!commonList.Contains(f))
                        commonList.Add(f);
                }
            }
            ViewData["List"] = commonList;
            return View();
        }
    }
}
