namespace home_light.Attributes
{
    /// <summary>
    /// Hide fields on swagger
    /// </summary>
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Method | AttributeTargets.Property)]
    public class SwaggerIgnoreAttribute : Attribute
    {

    }
}
