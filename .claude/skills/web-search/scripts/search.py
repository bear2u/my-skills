#!/usr/bin/env python3
"""DuckDuckGo Search CLI for Claude Code Skill."""

import argparse
import json
import subprocess
import sys


def ensure_dependency():
    try:
        import duckduckgo_search  # noqa: F401
    except ImportError:
        print("Installing duckduckgo-search...", file=sys.stderr)
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-U", "duckduckgo-search"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


def search_text(query, region, safesearch, timelimit, max_results):
    from duckduckgo_search import DDGS
    return list(DDGS().text(
        keywords=query,
        region=region,
        safesearch=safesearch,
        timelimit=timelimit,
        max_results=max_results,
    ))


def search_news(query, region, safesearch, timelimit, max_results):
    from duckduckgo_search import DDGS
    return list(DDGS().news(
        keywords=query,
        region=region,
        safesearch=safesearch,
        timelimit=timelimit,
        max_results=max_results,
    ))


def search_images(query, region, safesearch, max_results):
    from duckduckgo_search import DDGS
    return list(DDGS().images(
        keywords=query,
        region=region,
        safesearch=safesearch,
        max_results=max_results,
    ))


def main():
    parser = argparse.ArgumentParser(description="DuckDuckGo Search CLI")
    parser.add_argument("-q", "--query", required=True, help="검색 키워드")
    parser.add_argument(
        "-t", "--type", default="text",
        choices=["text", "news", "images"],
        help="검색 유형 (기본: text)",
    )
    parser.add_argument(
        "-n", "--max-results", type=int, default=5,
        help="최대 결과 수 (기본: 5)",
    )
    parser.add_argument(
        "-r", "--region", default="wt-wt",
        help="검색 지역 (기본: wt-wt)",
    )
    parser.add_argument(
        "-s", "--safesearch", default="moderate",
        choices=["on", "moderate", "off"],
        help="SafeSearch (기본: moderate)",
    )
    parser.add_argument(
        "-p", "--period", default=None,
        choices=["d", "w", "m", "y"],
        help="기간: d(일), w(주), m(월), y(년)",
    )
    args = parser.parse_args()

    ensure_dependency()

    try:
        if args.type == "text":
            results = search_text(
                args.query, args.region, args.safesearch,
                args.period, args.max_results,
            )
        elif args.type == "news":
            results = search_news(
                args.query, args.region, args.safesearch,
                args.period, args.max_results,
            )
        elif args.type == "images":
            results = search_images(
                args.query, args.region, args.safesearch,
                args.max_results,
            )

        output = {
            "query": args.query,
            "type": args.type,
            "region": args.region,
            "result_count": len(results),
            "results": results,
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))

    except Exception as e:
        error_output = {
            "error": True,
            "error_type": type(e).__name__,
            "message": str(e),
        }
        print(json.dumps(error_output, ensure_ascii=False, indent=2), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
