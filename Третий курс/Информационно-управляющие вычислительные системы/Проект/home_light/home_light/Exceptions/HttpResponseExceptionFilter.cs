using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;

namespace home_light.Exceptions;
/// <summary>
/// Http error handler user errors
/// </summary>
public class HttpResponseExceptionFilter : IActionFilter, IOrderedFilter
{
    /// <summary>
    /// Order default set int.MaxValue - 10
    /// </summary>
    public int Order => int.MaxValue - 10;
    /// <summary>
    /// On Action Executing
    /// </summary>
    /// <param name="context"></param>
    public void OnActionExecuting(ActionExecutingContext context) { }
    /// <summary>
    /// On Action Executed
    /// </summary>
    /// <param name="context"></param>
    public void OnActionExecuted(ActionExecutedContext context)
    {
        if (context.Exception is AccessErrorException httpResponseException)
        {
            var result = new ObjectResult(new
            {
                code = 500,
                message = httpResponseException.Message
            });
            result.StatusCode = 500;
            context.Result = result;
            context.ExceptionHandled = true;
        }
    }
}