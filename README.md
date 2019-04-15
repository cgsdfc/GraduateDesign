# BUAAthesis

北航毕设论文LaTeX模板

## 依赖

模板依赖v2.0及以上版本的ctex包，请使用较新版本的LaTeX发行版。

目前已经测试的LaTeX发行版包括：

+ TeXLive 2016、TeXLive 2017（**推荐**）
+ CTeX 2.9.3

对于老版本的LaTeX发行版，请通过包管理器升级ctex的版本。

## 具体说明-适用于计算机学院

本毕设模板是从北航开源俱乐部的Latex模板修改而来的，但是模板本身有一些小错误，并且不适用于计算机学院的论文格式要求。

修改如下：

1. 删除`buaathesis.bst` 中的：

```
FUNCTION {format.addr.pub}
{ publisher empty$
    {address empty$
        { ".[S.l.]: [s.n.] " *}
        { address ": [s.n.] " * }
        if$
    }
    { address empty$
        { ".[S.l.]: " * }
        { address ": " * }
        if$
        publisher *
    }

    if$
}

FUNCTION {format.caddr.pub}
{publisher empty$
    {address empty$
        { ".[出版地不详]：[出版者不详]" *}
        { address ":[出版者不详]" * }
        if$
    }
    { address empty$
        { ".[出版地不详]：" * }
        { address ": " * }
        if$
        publisher *
    }

    if$
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
FUNCTION {format.addr.institution}
{ institution empty$
    {address empty$
        { ".[S.l.]: [s.n.] " *}
        { address ": [s.n.] " * }
        if$
    }
    { address empty$
        { ".[S.l.]: " * }
        { address ": " * }
        if$
        institution *
    }

    if$
}

FUNCTION {format.caddr.institution}
{institution empty$
    {address empty$
        { ".[地址不详]：[机构不详]" *}
        { address ":[机构不详]" * }
        if$
    }
    { address empty$
        { ".[地址不详]：" * }
        { address ": " * }
        if$
        institution *
    }

    if$
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
FUNCTION {format.school.pub}
{ school empty$
    {address empty$
        { "[S.l.]: [s.n.] " }
        { address ": [s.n.] " * }
        if$
    }
    { address empty$
        { ".[S.l.]: " * }
        { address ": " * }
        if$
        school *
    }

    if$
}

FUNCTION {format.cschool.pub}
{school empty$
    {address empty$
        { "[地址不详]：[学校不详]" }
        { address ":[学校不详]" * }
        if$
    }
    { address empty$
        { ".[学校不详]：" * }
        { address ": " * }
        if$
        school *
    }

    if$
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
FUNCTION {format.inproceedings.addr.pub}
{
    TypeofLit empty$
    {publisher empty$
        {address empty$
            { ".[S.l.]: [s.n.] " }
            { address ": [s.n.] " * }
            if$
        }
        { address empty$
            { ".[S.l.]: " * }
            { address ": " * }
            if$
            publisher *
        }

        if$}
    { "" }
    if$
}

FUNCTION {format.cinproceedings.addr.pub}
{
    TypeofLit empty$
    {publisher empty$
        {address empty$
            { ".[出版地不详]：[出版者不详]" }
            { address ":[出版者不详]" * }
            if$
        }
        { address empty$
            { ".[出版地不详]：" * }
            { address ": " * }
            if$
            publisher *
        }

        if$}
    { ""}
    if$

}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
FUNCTION {format.misc.addr.pub}
{ publisher empty$
    {address empty$
        { "" }
        { address ": [s.n.] " * }
        if$
    }
    { address empty$
        { "[S.l.]: " * }
        { address ": " * }
        if$
        publisher *
    }

    if$
}

FUNCTION {format.cmisc.addr.pub}
{publisher empty$
    {address empty$
        { "" }
        { address ":[出版者不详]" * }
        if$
    }
    { address empty$
        { "[出版地不详]：" * }
        { address ": " * }
        if$
        publisher *
    }

    if$
}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


FUNCTION {format.addr.pub.org}                              %  If there's an
{ address empty$                                            %  an organization
    { "[S.l.]:" * publisher * ", for " * organization * }                 %  and a publisher
    { address ": " * publisher * ", for " * organization * }  %  too.
    if$
}

FUNCTION {format.addr.inst}
{ address empty$
    { institution empty$
        { "[S.l.]" }
        { "[S.l.]" * institution *}
        if$
    }
    { institution empty$
        { "" }
        { institution ", " * }
        if$
        address *
    }
    if$
}
```

2. `buaathesis.cls` 文件中，关于注释、目录的颜色已更改为False：

```latex
\DeclareOption{color}{\buaa@colorfalse}
```

3. `sample-bachelor.tex` 文件中，Latex的页边距设置可能要比word大，正文页间距建议值如下，更适合打印纸质版：

```latex
% 正文
\newgeometry{a4paper,left=3cm,right=2cm,top=3cm,bottom=3cm}
% bottom值建议为2.75-3.0cm之间
```

## 致谢

计算机学院14级 刘恒睿

计算机学院14级 田争曦