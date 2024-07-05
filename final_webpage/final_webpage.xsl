<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html" encoding="UTF-8"/>
    
    <xsl:template match="/corpus">
        <html lang="en">
            <head>
                <title>Bibliography of ACL papers</title>
                <style>
                    body {
                        background-color: #FFFFFA;
                    }
                    .h0 {
                        font-family: Geneva;
                        color: #800000;
                        font-size: 40px;
                        letter-spacing: 5px;
                        text-align: center;
                        padding-top: 1px;
                    }
                    .box {
                        display: inline-block;
                        width: 20px;
                        height: 20px;
                        margin-right: 5px;
                        margin-left: 20px;
                    }
                    .faketab {
                        margin-right: 15px;
                    }
                    h1 {
                        font-family: Helvetica, sans-serif;
                        color: #c46060;
                        padding-top: 25px;
                    }
                    p,
                    figcaption {
                        font-family: Helvetica, sans-serif;
                        line-height: 1.7;
                        text-align: justify;
                    }
                    li {
                        font-family: Helvetica, sans-serif;
                        line-height: 1.7;
                        padding-left: 8px;
                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                    }
                    th,
                    td {
                        border: 1px solid black;
                        padding: 8px;
                        text-align: left;
                    }
                    a:link,
                    a:visited {
                        color: #1d1d51;
                    }
                </style>
            </head>
            <body>
                <header>
                    <h1 style="text-align: left;" class="h0">Bibliography of ACL papers</h1>
                </header>
                <p>This website provides an overview of a selection of papers of the Association for Computational Linguistics. The papers are sorted into decade bins and highlighted by topic.</p>
                <h3>Choose by decade bin:</h3>
                <ul style="list-style-type: circle;">
                    <li style="font-family: Helvetica, sans-serif">
                        <a href="#1">2011 - Current</a>
                    </li>
                    <li style="font-family: Helvetica, sans-serif">
                        <a href="#2">2001 - 2010</a>
                    </li>
                    <li style="font-family: Helvetica, sans-serif">
                        <a href="#3">1991 - 2000</a>
                    </li>
                    <li style="font-family: Helvetica, sans-serif">
                        <a href="#4">1971 - 1990</a>
                    </li>
                    <li style="font-family: Helvetica, sans-serif">
                        <a href="#5">1952 - 1970</a>
                    </li>
                </ul>
                <hr width="100%" style="border-color: #c46060" align="left" size="2"/>
                <p>
                    Color Codes:
                    <span class="faketab">
                        <span class="box" style="background-color: rgb(237, 153, 227);"></span> Language Model
                    </span>
                    <span class="faketab">
                        <span class="box" style="background-color: rgb(133, 139, 217);"></span> Classification
                    </span>
                    <span class="faketab">
                        <span class="box" style="background-color: rgb(245, 153, 153);"></span> Corpora
                    </span>
                    <span class="faketab">
                        <span class="box" style="background-color: rgb(159, 222, 157);"></span> Evaluation
                    </span>
                    <span class="faketab">
                        <span class="box" style="background-color: rgb(246, 217, 143);"></span> Language-specific
                    </span>
                    <span class="faketab">
                        <span class="box" style="background-color: rgb(125, 216, 213);"></span> Other
                    </span>
                </p>
                
                <!-- Decade sections -->
                <h1 id="1">2011 - Current</h1>
                <p>
                    <table border="1">
                        <tr class="heading">
                            <th>Year</th>
                            <th>Title</th>
                            <th>Author(s)</th>
                            <th>URL</th>
                        </tr>
                        <xsl:for-each select="entry[dateInfo/year > 2010]">
                            <xsl:if test="position() &lt;= 20">
                                <tr>
                                    <td><xsl:value-of select="dateInfo/year"/></td>
                                    <xsl:choose>
                                        <xsl:when test="extraInfo/topic = 'language model'">
                                            <td bgcolor="#ED99E3">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'classification'">
                                            <td bgcolor="#858BD9">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'corpora'">
                                            <td bgcolor="#F59999">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'evaluation'">
                                            <td bgcolor="#9FDE9D">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'language specific'">
                                            <td bgcolor="#F6D98F">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'catch_all'">
                                            <td bgcolor="#7DD8D5">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <td>
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                    <td><xsl:value-of select="basicInfo/author"/></td>
                                    <td><a href="{extraInfo/url}"><xsl:value-of select="extraInfo/url"/></a></td>
                                </tr>
                            </xsl:if>
                        </xsl:for-each>
                    </table>
                </p>
                
                <h1 id="2">2001 - 2010</h1>
                <p>
                    <table border="1">
                        <tr class="heading">
                            <th>Year</th>
                            <th>Title</th>
                            <th>Author(s)</th>
                            <th>URL</th>
                        </tr>
                        <xsl:for-each select="entry[dateInfo/year > 2000 and dateInfo/year &lt;= 2010]">
                            <xsl:if test="position() &lt;= 20">
                                <tr>
                                    <td><xsl:value-of select="dateInfo/year"/></td>
                                    <xsl:choose>
                                        <xsl:when test="extraInfo/topic = 'language model'">
                                            <td bgcolor="#ED99E3">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'classification'">
                                            <td bgcolor="#858BD9">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'corpora'">
                                            <td bgcolor="#F59999">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'evaluation'">
                                            <td bgcolor="#9FDE9D">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'language specific'">
                                            <td bgcolor="#F6D98F">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'catch_all'">
                                            <td bgcolor="#7DD8D5">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <td>
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                    <td><xsl:value-of select="basicInfo/author"/></td>
                                    <td><a href="{extraInfo/url}"><xsl:value-of select="extraInfo/url"/></a></td>
                                </tr>
                            </xsl:if>
                        </xsl:for-each>
                    </table>
                </p>
                
                <h1 id="3">1991 - 2000</h1>
                <p>
                    <table border="1">
                        <tr class="heading">
                            <th>Year</th>
                            <th>Title</th>
                            <th>Author(s)</th>
                            <th>URL</th>
                        </tr>
                        <xsl:for-each select="entry[dateInfo/year > 1990 and dateInfo/year &lt;= 2000]">
                            <xsl:if test="position() &lt;= 20">
                                <tr>
                                    <td><xsl:value-of select="dateInfo/year"/></td>
                                    <xsl:choose>
                                        <xsl:when test="extraInfo/topic = 'language model'">
                                            <td bgcolor="#ED99E3">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'classification'">
                                            <td bgcolor="#858BD9">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'corpora'">
                                            <td bgcolor="#F59999">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'evaluation'">
                                            <td bgcolor="#9FDE9D">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'language specific'">
                                            <td bgcolor="#F6D98F">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'catch_all'">
                                            <td bgcolor="#7DD8D5">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <td>
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                    <td><xsl:value-of select="basicInfo/author"/></td>
                                    <td><a href="{extraInfo/url}"><xsl:value-of select="extraInfo/url"/></a></td>
                                </tr>
                            </xsl:if>
                        </xsl:for-each>
                    </table>
                </p>
                
                <h1 id="4">1971 - 1990</h1>
                <p>
                    <table border="1">
                        <tr class="heading">
                            <th>Year</th>
                            <th>Title</th>
                            <th>Author(s)</th>
                            <th>URL</th>
                        </tr>
                        <xsl:for-each select="entry[dateInfo/year > 1970 and dateInfo/year &lt;= 1990]">
                            <xsl:if test="position() &lt;= 20">
                                <tr>
                                    <td><xsl:value-of select="dateInfo/year"/></td>
                                    <xsl:choose>
                                        <xsl:when test="extraInfo/topic = 'language model'">
                                            <td bgcolor="#ED99E3">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'classification'">
                                            <td bgcolor="#858BD9">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'corpora'">
                                            <td bgcolor="#F59999">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'evaluation'">
                                            <td bgcolor="#9FDE9D">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'language specific'">
                                            <td bgcolor="#F6D98F">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'catch_all'">
                                            <td bgcolor="#7DD8D5">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <td>
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                    <td><xsl:value-of select="basicInfo/author"/></td>
                                    <td><a href="{extraInfo/url}"><xsl:value-of select="extraInfo/url"/></a></td>
                                </tr>
                            </xsl:if>
                        </xsl:for-each>
                    </table>
                </p>
                
                <h1 id="5">1952 - 1970</h1>
                <p>
                    <table border="1">
                        <tr class="heading">
                            <th>Year</th>
                            <th>Title</th>
                            <th>Author(s)</th>
                            <th>URL</th>
                        </tr>
                        <xsl:for-each select="entry[dateInfo/year &gt;= 1952 and dateInfo/year &lt;= 1970]">
                            <xsl:if test="position() &lt;= 20">
                                <tr>
                                    <td><xsl:value-of select="dateInfo/year"/></td>
                                    <xsl:choose>
                                        <xsl:when test="extraInfo/topic = 'language model'">
                                            <td bgcolor="#ED99E3">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'classification'">
                                            <td bgcolor="#858BD9">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'corpora'">
                                            <td bgcolor="#F59999">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'evaluation'">
                                            <td bgcolor="#9FDE9D">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'language specific'">
                                            <td bgcolor="#F6D98F">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:when test="extraInfo/topic = 'catch_all'">
                                            <td bgcolor="#7DD8D5">
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <td>
                                                <xsl:value-of select="basicInfo/title"/>
                                            </td>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                    <td><xsl:value-of select="basicInfo/author"/></td>
                                    <td><a href="{extraInfo/url}"><xsl:value-of select="extraInfo/url"/></a></td>
                                </tr>
                            </xsl:if>
                        </xsl:for-each>
                    </table>
                </p>
                
                <hr width="23%" style="border-color: #c46060" align="left" size="1"/>
                
                <footer>
                    <p>
                        <span style="font-family: Helvetica, sans-serif; color: #800000; font-size: larger;">
                            <strong>Authors of the website: </strong>
                        </span>
                        Tana Deeg, Momo Takamatsu, Sandro Weick
                    </p>
                </footer>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
